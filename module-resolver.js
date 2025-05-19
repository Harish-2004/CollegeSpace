const path = require('path');

// Add the root node_modules to the module search path
const rootNodeModules = path.resolve(__dirname, 'node_modules');
require.resolve = function(specifier) {
  return path.resolve(rootNodeModules, specifier);
}; 