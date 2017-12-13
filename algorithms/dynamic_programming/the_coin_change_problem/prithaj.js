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

function makeChange(c, n, m, cache){
    // Complete this function
    if (n===0){
        return 1;
    }
    if(n<0){
        return 0;
    }
    if(m<=0 & n>=1 ){
       return 0;
       }
    if(n+','+m in cache){
        return cache[n+','+m];
    }
    cache[n+','+m] = makeChange(c, n-c[m-1], m, cache)+makeChange(c, n, m-1, cache);
    return cache[n+','+m];
}

function main() {
    var n_temp = readLine().split(' ');
    var n = parseInt(n_temp[0]);
    var m = parseInt(n_temp[1]);
    var cache = {}
    var c = readLine().split(' ').map(Number);
    var ways = makeChange(c, n, m, cache);
    console.log(ways);

}