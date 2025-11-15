"""Utilidades para el portafolio: optimización de imágenes, thumbnails, etc."""

from PIL import Image
from django.core.files.base import ContentFile
import os


def optimize_image(image_path, max_width=1920, quality=85):
    """
    Optimiza una imagen: redimensiona y comprime.

    Args:
        image_path (str): Ruta absoluta de la imagen
        max_width (int): Ancho máximo en píxeles
        quality (int): Calidad JPEG (0-100)
    """
    if not os.path.exists(image_path):
        return False

    try:
        image = Image.open(image_path)

        # Convertir a RGB si es necesario (para JPEG)
        if image.mode in ('RGBA', 'LA', 'P'):
            rgb_image = Image.new('RGB', image.size, (255, 255, 255))
            rgb_image.paste(image, mask=image.split()[-1] if image.mode == 'RGBA' else None)
            image = rgb_image

        # Redimensionar si es más ancho que max_width
        if image.width > max_width:
            ratio = max_width / image.width
            new_height = int(image.height * ratio)
            image = image.resize((max_width, new_height), Image.Resampling.LANCZOS)

        # Guardar optimizado
        image.save(image_path, 'JPEG', quality=quality, optimize=True)
        return True
    except Exception as e:
        print(f"Error al optimizar imagen {image_path}: {e}")
        return False


def create_thumbnail(image_path, thumbnail_path, size=(300, 300)):
    """
    Crea una miniatura a partir de una imagen.

    Args:
        image_path (str): Ruta de la imagen original
        thumbnail_path (str): Ruta donde guardar la miniatura
        size (tuple): Tamaño de la miniatura (ancho, alto)

    Returns:
        bool: True si se creó con éxito
    """
    if not os.path.exists(image_path):
        return False

    try:
        image = Image.open(image_path)

        # Convertir a RGB si es necesario
        if image.mode in ('RGBA', 'LA', 'P'):
            rgb_image = Image.new('RGB', image.size, (255, 255, 255))
            rgb_image.paste(image, mask=image.split()[-1] if image.mode == 'RGBA' else None)
            image = rgb_image

        # Crear miniatura con proporción
        image.thumbnail(size, Image.Resampling.LANCZOS)

        # Guardar miniatura
        image.save(thumbnail_path, 'JPEG', quality=80, optimize=True)
        return True
    except Exception as e:
        print(f"Error al crear thumbnail {thumbnail_path}: {e}")
        return False


def convert_to_webp(image_path):
    """
    Convierte una imagen a WebP para mejor compresión.

    Args:
        image_path (str): Ruta de la imagen original

    Returns:
        str: Ruta de la imagen en WebP, o None si falla
    """
    if not os.path.exists(image_path):
        return None

    try:
        image = Image.open(image_path)

        # Convertir a RGB si es necesario
        if image.mode in ('RGBA', 'LA', 'P'):
            rgb_image = Image.new('RGB', image.size, (255, 255, 255))
            rgb_image.paste(image, mask=image.split()[-1] if image.mode == 'RGBA' else None)
            image = rgb_image

        webp_path = os.path.splitext(image_path)[0] + '.webp'
        image.save(webp_path, 'WEBP', quality=80)
        return webp_path
    except Exception as e:
        print(f"Error al convertir a WebP {image_path}: {e}")
        return None
