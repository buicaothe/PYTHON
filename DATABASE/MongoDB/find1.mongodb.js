/* global use */
// MongoDB Playground
// Use Ctrl+Space inside a snippet or a string literal to trigger completions.

// The current database to use.
use("myBuiCaoTheDB");

db.library.find({ price: { $gt: 15 } }, { title: 1, price: 1 })