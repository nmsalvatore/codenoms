const path = require("path");

module.exports = {
  mode: "development",
  entry: {
    tiptap: "./js/tiptap.js",
    hljs: "./js/hljs.js",
  },
  output: {
    filename: "[name].bundle.js",
    path: path.resolve(__dirname, "..", "static", "js"),
  },
};
