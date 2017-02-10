process.stdin.resume();
process.stdin.setEncoding('ascii');

var input_stdin = "";
var input_stdin_array = "";
var input_currentline = 0;

process.stdin.on('data', function (data) {
    input_stdin += data;
});

process.stdin.on('end', function () {
    input_stdin_array = input_stdin.split("\n");
    main();    
});

function readLine() {
    return input_stdin_array[input_currentline++];
}

/////////////// ignore above this line ////////////////////

function main() {
    var n = parseInt(readLine());
    var a_sum = 0;
    var b_sum = 0;
    for(a_i = 0; a_i < n; a_i++){
       a = readLine().split(' ').map(Number);
       a_sum = a_sum + a[a_i];
       b_sum = b_sum + a[n-a_i-1];
    }
    console.log(Math.abs(a_sum-b_sum));
}