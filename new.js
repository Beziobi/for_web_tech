var myname = "Beau"
myname += " no  my name is bisrat "
console.log(myname)
console.log(myname[0])
console.log(myname[myname.length - 1])

function wordBlanks (myNoun, myAdjective, myVerb, myAdverb)
{
    var result = ""
    result += "The " +  myAdjective + " " +  myNoun + " " + myVerb + " to the store " + myAdverb
    
    return result 
}

console.log(wordBlanks ("dog", "big", "ran", "quickly"))



// store in side array 

var outArray = ["John" , 23 ]
var mydata = outArray[0]
console.log(mydata)

// nested array

var ourArray = [ ["the universe" ,42 ] , ["binary is only " , " 101010"]]

console.log(ourArray [0][0])

// push 
// will push new index to array 

var pusharray = ["stimpson " , "J"]
// pusharray.push("new")
// console.log(pusharray[2])

// pop 
// will remove the last index form the array 

var newarray = pusharray.pop


console.log (newarray)






