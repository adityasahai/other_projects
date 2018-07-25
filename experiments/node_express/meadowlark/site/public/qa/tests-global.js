var chai = require('chai');

suite('Global Tests', () => {
    test('page has a valid title', () => {
        chai.assert.isTrue(document.title && document.title.match(/\S/) &&
                document.title.toUpperCase() !== 'TODO');
    });
});