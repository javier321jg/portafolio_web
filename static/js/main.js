/**
 * Main JavaScript - Portafolio Nelson
 * Animaciones, interacciones y utilidades globales
 */

// ================================
// Configuración Global
// ================================

const config = {
    animationDuration: 0.6,
    scrollTriggerOffset: '80%',
    navbarScrollThreshold: 50,
};

// ================================
// Navbar Scroll Effect
// ================================

document.addEventListener('DOMContentLoaded', function () {
    const navbar = document.getElementById('navbar');
    const mobileMenuBtn = document.getElementById('mobile-menu-btn');
    const mobileMenu = document.getElementById('mobile-menu');

    // Navbar scroll effect
    window.addEventListener('scroll', function () {
        if (window.scrollY > config.navbarScrollThreshold) {
            navbar?.classList.add('navbar-scrolled');
        } else {
            navbar?.classList.remove('navbar-scrolled');
        }
    });

    // Mobile menu toggle
    if (mobileMenuBtn) {
        mobileMenuBtn.addEventListener('click', function () {
            mobileMenu?.classList.toggle('hidden');
        });

        // Cerrar menú al hacer click en un enlace
        const mobileMenuLinks = mobileMenu?.querySelectorAll('a');
        mobileMenuLinks?.forEach(link => {
            link.addEventListener('click', function () {
                mobileMenu?.classList.add('hidden');
            });
        });
    }
});

// ================================
// GSAP ScrollTrigger Animations
// ================================

if (typeof gsap !== 'undefined') {
    gsap.registerPlugin(ScrollTrigger);

    // Animar elementos con clase fade-in
    gsap.utils.toArray('.fade-in').forEach((el) => {
        gsap.from(el, {
            opacity: 0,
            y: 30,
            duration: config.animationDuration,
            scrollTrigger: {
                trigger: el,
                start: `top ${config.scrollTriggerOffset}`,
            }
        });
    });

    // Animar tarjetas de proyectos
    gsap.utils.toArray('.project-card').forEach((card, index) => {
        gsap.to(card, {
            opacity: 1,
            y: 0,
            duration: config.animationDuration,
            delay: index * 0.1,
            scrollTrigger: {
                trigger: card,
                start: `top ${config.scrollTriggerOffset}`,
            }
        });
    });

    // Animar tarjetas de logros
    gsap.utils.toArray('.achievement-card').forEach((card, index) => {
        gsap.to(card, {
            opacity: 1,
            y: 0,
            duration: config.animationDuration,
            delay: index * 0.15,
            scrollTrigger: {
                trigger: card,
                start: `top 85%`,
            }
        });
    });

    // Animar tarjetas de habilidades
    gsap.utils.toArray('.skill-card').forEach((card, index) => {
        gsap.to(card, {
            opacity: 1,
            y: 0,
            duration: config.animationDuration,
            delay: index * 0.08,
            scrollTrigger: {
                trigger: card,
                start: `top ${config.scrollTriggerOffset}`,
            }
        });
    });
}

// ================================
// Smooth Scroll para Anchor Links
// ================================

document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const targetId = this.getAttribute('href');
        const target = document.querySelector(targetId);

        if (target) {
            target.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    });
});

// ================================
// Inicializar Swiper
// ================================

function initializeSwipers() {
    // Tech Slider
    if (document.querySelector('.tech-slider')) {
        new Swiper('.tech-slider', {
            slidesPerView: 1,
            spaceBetween: 30,
            pagination: {
                el: '.swiper-pagination',
                clickable: true,
            },
            breakpoints: {
                640: {
                    slidesPerView: 2,
                    spaceBetween: 20,
                },
                1024: {
                    slidesPerView: 5,
                    spaceBetween: 20,
                }
            },
            autoplay: {
                delay: 3000,
                disableOnInteraction: false,
            },
            loop: true,
        });
    }

    // Galería de Proyectos
    if (document.querySelector('.gallery-slider')) {
        new Swiper('.gallery-slider', {
            slidesPerView: 1,
            spaceBetween: 20,
            pagination: {
                el: '.swiper-pagination',
                clickable: true,
            },
            navigation: {
                nextEl: '.swiper-button-next',
                prevEl: '.swiper-button-prev',
            },
            breakpoints: {
                768: {
                    slidesPerView: 2,
                },
                1024: {
                    slidesPerView: 3,
                }
            },
        });
    }
}

// Inicializar Swipers cuando el documento esté listo
document.addEventListener('DOMContentLoaded', initializeSwipers);

// ================================
// Hover Effects en Imágenes
// ================================

document.querySelectorAll('.hover-glow img').forEach(img => {
    img.addEventListener('mouseenter', function () {
        this.style.transform = 'scale(1.05)';
    });

    img.addEventListener('mouseleave', function () {
        this.style.transform = 'scale(1)';
    });
});

// ================================
// Lightbox Modal para Imágenes
// ================================

class ImageLightbox {
    constructor() {
        this.currentIndex = 0;
        this.images = [];
        this.init();
    }

    init() {
        // Crear modal
        const modal = document.createElement('div');
        modal.id = 'lightbox-modal';
        modal.className = 'hidden fixed inset-0 z-50 bg-black/80 flex items-center justify-center';
        modal.innerHTML = `
            <div class="relative max-w-4xl w-full h-5/6">
                <img id="lightbox-image" class="w-full h-full object-contain" src="" alt="">
                <button id="lightbox-close" class="absolute top-4 right-4 bg-white rounded-full w-10 h-10 flex items-center justify-center">
                    <span>&times;</span>
                </button>
                <button id="lightbox-prev" class="absolute left-4 top-1/2 transform -translate-y-1/2 bg-white rounded-full w-10 h-10 flex items-center justify-center">
                    &lt;
                </button>
                <button id="lightbox-next" class="absolute right-4 top-1/2 transform -translate-y-1/2 bg-white rounded-full w-10 h-10 flex items-center justify-center">
                    &gt;
                </button>
            </div>
        `;
        document.body.appendChild(modal);

        // Eventos
        const closeBtn = modal.querySelector('#lightbox-close');
        const prevBtn = modal.querySelector('#lightbox-prev');
        const nextBtn = modal.querySelector('#lightbox-next');

        closeBtn?.addEventListener('click', () => this.close());
        prevBtn?.addEventListener('click', () => this.prev());
        nextBtn?.addEventListener('click', () => this.next());
        modal.addEventListener('click', (e) => {
            if (e.target === modal) this.close();
        });
    }

    open(images, startIndex = 0) {
        this.images = images;
        this.currentIndex = startIndex;
        const modal = document.getElementById('lightbox-modal');
        modal?.classList.remove('hidden');
        this.show();
    }

    close() {
        const modal = document.getElementById('lightbox-modal');
        modal?.classList.add('hidden');
    }

    show() {
        const image = document.getElementById('lightbox-image');
        if (image && this.images[this.currentIndex]) {
            image.src = this.images[this.currentIndex];
        }
    }

    next() {
        this.currentIndex = (this.currentIndex + 1) % this.images.length;
        this.show();
    }

    prev() {
        this.currentIndex = (this.currentIndex - 1 + this.images.length) % this.images.length;
        this.show();
    }
}

// Inicializar lightbox
const lightbox = new ImageLightbox();

// Agregar listeners a imágenes de galería
document.querySelectorAll('.gallery-item img').forEach((img, index) => {
    img.style.cursor = 'pointer';
    img.addEventListener('click', function () {
        const images = Array.from(document.querySelectorAll('.gallery-item img')).map(i => i.src);
        lightbox.open(images, index);
    });
});

// ================================
// Lazy Loading (si no hay soporte nativo)
// ================================

if ('IntersectionObserver' in window) {
    const imageObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const img = entry.target;
                img.src = img.dataset.src || img.src;
                img.classList.remove('lazy');
                observer.unobserve(img);
            }
        });
    });

    document.querySelectorAll('img[data-src]').forEach(img => {
        imageObserver.observe(img);
    });
}

// ================================
// Form Validation & Submission
// ================================

const contactForm = document.getElementById('contact-form');
if (contactForm) {
    contactForm.addEventListener('submit', function (e) {
        // Aquí Django manejará la validación y envío
        // Este código es solo para efectos visuales
        const submitBtn = this.querySelector('button[type="submit"]');
        if (submitBtn) {
            submitBtn.disabled = true;
            submitBtn.textContent = 'Enviando...';
        }
    });
}

// ================================
// Detección de Tema Oscuro
// ================================

function checkDarkMode() {
    if (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) {
        document.documentElement.classList.add('dark');
    }
}

checkDarkMode();

// Escuchar cambios en las preferencias del sistema
if (window.matchMedia) {
    window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', e => {
        if (e.matches) {
            document.documentElement.classList.add('dark');
        } else {
            document.documentElement.classList.remove('dark');
        }
    });
}

// ================================
// Utilidades y Helpers
// ================================

// Debounce function
function debounce(func, wait) {
    let timeout;
    return function (...args) {
        clearTimeout(timeout);
        timeout = setTimeout(() => func.apply(this, args), wait);
    };
}

// Throttle function
function throttle(func, limit) {
    let inThrottle;
    return function (...args) {
        if (!inThrottle) {
            func.apply(this, args);
            inThrottle = true;
            setTimeout(() => inThrottle = false, limit);
        }
    };
}

// Copiar al portapapeles
function copyToClipboard(text) {
    if (navigator.clipboard) {
        navigator.clipboard.writeText(text).then(() => {
            console.log('Copiado al portapapeles');
        });
    }
}

// ================================
// Performance Monitoring
// ================================

if (window.performance && window.performance.timing) {
    window.addEventListener('load', function () {
        const perfData = window.performance.timing;
        const pageLoadTime = perfData.loadEventEnd - perfData.navigationStart;
        console.log('Tiempo de carga total: ' + pageLoadTime + 'ms');
    });
}

// ================================
// Event Listeners Globales
// ================================

// Manejar cambios de tamaño de ventana
window.addEventListener('resize', debounce(() => {
    // Reinitialize components si es necesario
    if (typeof ScrollTrigger !== 'undefined') {
        ScrollTrigger.refresh();
    }
}, 250));

// Prevent FOUC (Flash of Unstyled Content)
document.documentElement.classList.add('loading');
window.addEventListener('load', () => {
    document.documentElement.classList.remove('loading');
});

console.log('%cPortafolio Nelson Javier Gutierrez Ramos', 'font-size: 20px; color: #00d4ff; font-weight: bold;');
console.log('%cDiseño de alto impacto visual con Django y tecnologías web modernas', 'color: #00ff88;');
