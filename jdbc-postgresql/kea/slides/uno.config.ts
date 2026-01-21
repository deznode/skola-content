import { defineConfig } from 'unocss'

export default defineConfig({
  theme: {
    colors: {
      // Skola.dev Brand Colors
      skola: {
        ocean: '#0077B6',      // Primary - headers, links
        yellow: '#FFC300',     // Accent - highlights, CTAs
        sand: '#F4EBD0',       // Background - light sections
        navy: '#001F3F',       // Dark text, dark mode bg
        coral: '#FF595E',      // Warnings, errors
        teal: '#2A9D8F',       // Success, code highlights
        gray: '#4A5D73',       // Secondary text
      },
    },
  },
  shortcuts: {
    // Skola brand shortcuts
    'skola-heading': 'text-skola-ocean font-bold',
    'skola-accent': 'text-skola-yellow',
    'skola-warning': 'text-skola-coral font-bold',
    'skola-success': 'text-skola-teal',
    'skola-muted': 'text-skola-gray opacity-75',
    'skola-bg-light': 'bg-skola-sand',
    'skola-bg-dark': 'bg-skola-navy',
  },
})
