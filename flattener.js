// input is a list of lists of n layers
// output is a single layer list

//as solution is recursive, there is no need ot manually compute the depth of the input list of lists
var memo = []
function flattener(list){
    for(var i=0; i<list.length; i++){
        if(typeof list[i] == "number") memo.push(list[i])
        else{
            flattener(list[i])
        }
    } 

return memo    

}

const flattened = flattener([1, 2, [3, 4, [5, 6, [7, [8, 9, 10]]]]] )
console.log(flattened)