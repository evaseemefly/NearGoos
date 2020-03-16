module.exports = {
    // baseUrl: '/',
    chainWebpack:(config)=>{
      config.plugins.delete('fork-ts-checker') // 禁用fork-ts-checker
    },
  }