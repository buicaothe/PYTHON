/* global use */
// MongoDB Playground
// Use Ctrl+Space inside a snippet or a string literal to trigger completions.

// The current database to use.
use("myBuiCaoTheDB");

db.library.find({ $or: [{ price: { $gte: 10 } }, { $or: [{ price: { $gte: 10 } }, { price: { $lte: 40 }] }, { _id: 0, title: 1, author: 1, price: 1 }).sort({ price: 1 })