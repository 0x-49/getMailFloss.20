// @ts-check
import { defineConfig } from 'astro/config';
import react from '@astrojs/react';
import tailwind from '@astrojs/tailwind';
import icon from "astro-icon";

// https://astro.build/config
export default defineConfig({
  integrations: [
    react(),
    tailwind(),
    icon({
      include: {
        lucide: ['*'],
        "simple-icons": ["*"],
      }
    })
  ],
  server: {
    port: 3000,
    host: true // Expose to all network interfaces
  },
  vite: {
    server: {
      fs: {
        allow: ['..']
      }
    }
  }
});