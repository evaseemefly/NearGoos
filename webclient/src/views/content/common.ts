const isIEClient = (): boolean => {
  if (!!window.ActiveXObject || 'ActiveXObject' in window) {
    return true;
  } else {
    return false;
  }
};

export { isIEClient };
