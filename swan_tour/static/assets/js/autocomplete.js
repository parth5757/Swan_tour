new Autocomplete('#autocomplete', {
    search : input => {
        console.log(input)
        const url = `/get_name/?search=${input}`
        return new Promise(resolve =>{
            fetch(url)
            .then(response => response.json())
            .then(data => {
                console.log(data)
                resolve(data.data)
            });
        });
    },
})
// new Autocomplete('#search-destination', {
//     search: input => {
//         console.log(input)
//         const url = `/get-search/?search=${input}`; // Enclosed URL in backticks
//         return new Promise(resolve => {
//             fetch(url)
//                 .then(response => response.json())
//                 .then(data => {
//                     resolve(data.data);
//                 })
//                 .catch(error => {
//                     console.error('Error fetching data:', error);
//                     resolve([]);
//                 });
//         });
//     },
//     renderResult: (result, props) => {
//         const wrapper = document.createElement('div');
//         wrapper.classList.add('autocomplete-result');
//         wrapper.textContent = result;

//         const group = Math.floor(props.index / 3);
//         if (props.index % 3 === 0) {
//             const groupElement = document.createElement('li');
//             groupElement.classList.add('group');
//             groupElement.textContent = `Group ${group + 1}`;
//             wrapper.appendChild(groupElement);
//         }

//         return wrapper;
//     }
// });