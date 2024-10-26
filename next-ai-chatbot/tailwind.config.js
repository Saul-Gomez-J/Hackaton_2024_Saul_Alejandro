const { fontFamily } = require('tailwindcss/defaultTheme')

/** @type {import('tailwindcss').Config} */
module.exports = {
  darkMode: ['class'],
  content: ['app/**/*.{ts,tsx}', 'components/**/*.{ts,tsx}'],
  theme: {
    container: {
      center: true,
      padding: '2rem',
      screens: {
        '2xl': '1400px'
      }
    },
    extend: {
      fontFamily: {
        sans: ['var(--font-sans)', ...fontFamily.sans]
      },
      colors: {
        border: '#C8A27E',        // Café Latte
        input: '#C8A27E',         // Café Latte
        ring: '#C8A27E',          // Café Latte
        background: {
          DEFAULT: '#E8E0DA',     // Gris café suave
          dark: '#362420',        // Gris café oscuro
        },
        foreground: {
          DEFAULT: '#4B2E2B',     // Marrón Espresso
          dark: '#FFFFFF',        // Blanco para modo oscuro
        },
        primary: {
          DEFAULT: '#8F9D5A',     // Verde Hoja
          foreground: '#FFFFFF',  // Blanco
        },
        secondary: {
          DEFAULT: '#C8A27E',     // Café Latte
          foreground: '#4B2E2B',  // Marrón Espresso
        },
        destructive: {
          DEFAULT: '#991B1B',     // Rojo destructivo
          foreground: '#FEFEFE',  // Casi blanco
        },
        muted: {
          DEFAULT: '#F3E5AB',     // Crema suave
          foreground: '#5A5A5A',  // Gris Pizarra
        },
        accent: {
          DEFAULT: '#C8A27E',     // Café Latte
          foreground: '#4B2E2B',  // Marrón Espresso
        },
        popover: {
          DEFAULT: '#E8E0DA',     // Gris café suave
          foreground: '#4B2E2B',  // Marrón Espresso
        },
        card: {
          DEFAULT: '#E8E0DA',     // Gris café suave
          foreground: '#4B2E2B',  // Marrón Espresso
        }
      },
      borderRadius: {
        lg: '0.5rem',
        md: '0.375rem',
        sm: '0.25rem'
      },
      keyframes: {
        'accordion-down': {
          from: { height: 0 },
          to: { height: 'var(--radix-accordion-content-height)' }
        },
        'accordion-up': {
          from: { height: 'var(--radix-accordion-content-height)' },
          to: { height: 0 }
        },
        'slide-from-left': {
          '0%': {
            transform: 'translateX(-100%)'
          },
          '100%': {
            transform: 'translateX(0)'
          }
        },
        'slide-to-left': {
          '0%': {
            transform: 'translateX(0)'
          },
          '100%': {
            transform: 'translateX(-100%)'
          }
        }
      },
      animation: {
        'slide-from-left':
          'slide-from-left 0.3s cubic-bezier(0.82, 0.085, 0.395, 0.895)',
        'slide-to-left':
          'slide-to-left 0.25s cubic-bezier(0.82, 0.085, 0.395, 0.895)',
        'accordion-down': 'accordion-down 0.2s ease-out',
        'accordion-up': 'accordion-up 0.2s ease-out'
      }
    }
  },
  plugins: [require('tailwindcss-animate'), require('@tailwindcss/typography')]
}