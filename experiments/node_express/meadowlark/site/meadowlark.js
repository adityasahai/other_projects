const express = require('express');

const app = express();
// handlebars
const handlebars = require('express3-handlebars')
                    .create({defaultLayout: 'main'});

const fortunes = [
  "some fortune cookie",
  "what is happening?!"
];

app.engine('handlebars', handlebars.engine);
app.set('view engine', 'handlebars');

app.set('port', process.env.PORT || 3000);

app.use(express.static(__dirname + '/public'));

app.use((req, res, next) => {
  res.locals.showTests = app.get('env') !== 'production' &&
        req.query.test === '1';
  next();
});

app.listen(app.get('port'), () => {
  console.log('Express started on http://localhost:' + 
    app.get('port') + '; press Ctrl-C to terminate.');
});

app.get('/', (req, res) => {
  res.render('home');
});

app.get('/about', (req, res) => {
  var randomFortune = fortunes[Math.floor(Math.random() * fortunes.length)];
  res.render('about', {
    fortune: randomFortune,
    pageTestScript: 'qa/tests-about.js'
  });
});

app.use((req, res, next) => {
  res.status(404);
  res.render('404');
});

app.use((err, req, res, next) => {
  console.error(err.stack);
  res.status(500);
  res.render('500');
})
