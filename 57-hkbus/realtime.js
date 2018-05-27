const HKBus = require('hkbus')

const q = HKBus({
    lang: 'en',
    operator: 'kmb',  // only KMB is supported at the moment
    verbose: 0
  });


q.getStops('216M')
.then(stops => {
console.log('All Bounds');
console.log(JSON.stringify(stops));
})
.catch(console.error);

// q.getStops('3C', 1)
//   .then(console.log)
//   .then(stops => {
//     console.log('Bound 1 only');
//     console.log(JSON.stringify(stops));
//   })
//   .catch(console.error);
