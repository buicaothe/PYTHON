use('myBuiCaoTheDB');

db.library.updateOne({ name: "Libraryworker, Lisa" }, {{ title: { $regex: "^Reg" } }}
);