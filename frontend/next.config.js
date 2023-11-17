module.exports = {
    images: {
      formats: ['image/avif', 'image/webp'],
      domains: ['lh3.googleusercontent.com'],
      remotePatterns: [
        {
          protocol: 'https',
          hostname: 'assets.vercel.com',
          port: '',
          pathname: '/image/upload/**',
        },
      ],
    },
  }