use('sample_mflix');
db.movies.countDocuments({ title: /^Reg/ });