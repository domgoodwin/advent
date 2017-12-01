var fs = require('fs')

var filename = "inputs/day1.txt"

fs.readFile(filename, 'utf8', function(err, data){
  if(err){
    console.error(err);
    return;
  }
  console.log(data);
  var sum = 0;
  for (var i = 1, len = data.length; i < len + 1; i++) {
    var cur = parseInt(data[i]);
    if(i == data.length){
      if(cur == data[0]){
        console.log("I is: " + i + " cur is " + cur);
        sum += cur;
      }
    }else if(cur == data[getCircleNumber(i, data)]){
      console.log("Adding " + cur + " as using " + i + " and "  +  getCircleNumber(i, data));
      sum += cur;
    }
  }
  console.log("Sum part 1: " + sum);
  console.log("List length is " + data.length + " Last ele is: " + data[data.length - 1]);
});


function getCircleNumber(i, arr){
  var num = i + (arr.length / 2);
  if(num > arr.length){
    num = num - arr.length;
  }
  console.log("i, arrlen, num: " + i + "  " + arr.length + "  " + num);
  return num;
}
