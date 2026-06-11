document.addEventListener("DOMContentLoaded", (event) => {
    // Register GSAP ScrollTrigger
    gsap.registerPlugin(ScrollTrigger);

    // Generic reveal animation for sections
    gsap.utils.toArray('section:not(.hero):not(.welcome-row)').forEach(section => {
        gsap.fromTo(section, 
            { opacity: 0, y: 40 },
            { 
                opacity: 1, 
                y: 0, 
                duration: 1, 
                ease: "power3.out",
                scrollTrigger: {
                    trigger: section,
                    start: "top 85%",
                    toggleActions: "play none none none"
                }
            }
        );
    });

    // Staggered animation for cards
    const cardContainers = [
        '.benefits-grid', 
        '.steps-grid', 
        '.courses-grid', 
        '.quizzes-grid',
        '.quiz-levels-grid',
        '.stats-grid',
        '.topic-list',
        '.rec-list'
    ];

    cardContainers.forEach(selector => {
        const container = document.querySelector(selector);
        if (container) {
            const cards = container.children;
            gsap.fromTo(cards,
                { opacity: 0, y: 30 },
                {
                    opacity: 1,
                    y: 0,
                    duration: 0.8,
                    stagger: 0.15,
                    ease: "power2.out",
                    scrollTrigger: {
                        trigger: container,
                        start: "top 85%",
                        toggleActions: "play none none none"
                    }
                }
            );
        }
    });

    // Initial Load Timeline
    const tl = gsap.timeline();

    // Navbar animation
    const nav = document.querySelector('nav') || document.querySelector('header');
    if (nav) {
        tl.fromTo(nav, 
            { opacity: 0, y: -20 },
            { opacity: 1, y: 0, duration: 0.6, ease: "power2.out" }
        );

        const navElements = nav.querySelectorAll('.logo, .nav-links > li, .nav-buttons');
        if (navElements.length > 0) {
            tl.fromTo(navElements,
                { opacity: 0, y: -10 },
                { opacity: 1, y: 0, duration: 0.4, stagger: 0.1, ease: "power2.out" },
                "-=0.4"
            );
        } else {
            const headerElements = nav.children;
            tl.fromTo(headerElements,
                { opacity: 0, x: -10 },
                { opacity: 1, x: 0, duration: 0.4, stagger: 0.1, ease: "power2.out" },
                "-=0.4"
            );
        }
    }

    // Hero section intro synced with timeline
    const heroContent = document.querySelector('.hero-content');
    if (heroContent) {
        tl.fromTo(heroContent.children,
            { opacity: 0, y: 20 },
            {
                opacity: 1,
                y: 0,
                duration: 0.6,
                stagger: 0.15,
                ease: "power2.out",
            },
            "-=0.2"
        );
    }

    const heroVisual = document.querySelector('.hero-visual-new');
    if (heroVisual) {
        tl.fromTo(heroVisual,
            { opacity: 0, scale: 0.95, x: 30 },
            {
                opacity: 1,
                scale: 1,
                x: 0,
                duration: 0.8,
                ease: "power2.out",
            },
            "-=0.6"
        );
    }

    // Dashboard welcome section intro synced with timeline
    const welcomeRow = document.querySelector('.welcome-row');
    if (welcomeRow) {
        tl.fromTo(welcomeRow.children,
            { opacity: 0, x: -20 },
            {
                opacity: 1,
                x: 0,
                duration: 0.6,
                stagger: 0.2,
                ease: "power2.out",
            },
            "-=0.4"
        );
    }
});
