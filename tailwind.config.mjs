/** @type {import('tailwindcss').Config} */
export default {
  content: ['./src/**/*.{astro,html,js,jsx,md,mdx,svelte,ts,tsx,vue}'],
  theme: {
    extend: {
      container: {
        center: true,
        padding: '1rem',
      },
      colors: {
        primary: {
          50: '#edfaf8',
          100: '#d5f3ef',
          200: '#aee9e2',
          300: '#7ed7cd',
          400: '#4cbeb2',
          500: '#29a195',
          600: '#1f8278',
          700: '#1c6861',
          800: '#1a544f',
          900: '#184842',
        },
      },
    },
  },
  plugins: [],
}
