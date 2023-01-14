

module.exports = {
  experimental: {
    appDir: true,
  },
  swcMinify: true,
  reactStrictMode: true,
  compiler: {
    styledComponents: true,
  },
  // async rewrites() {
  //   return [
  //     {
  //       source: '/api/:path*',
  //       destination: 'http://localhost:3100/:path*'
  //     }
  //   ]
  // }
}