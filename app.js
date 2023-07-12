const { spawn } = require( 'child_process' );
var fs = require('fs');


// const testFolder = './pImages/';
// var names=[];

// fs.readdirSync( testFolder ).forEach( file =>
// {
//     names.push(file);
   

// } );

// let listItems  = Object.values(names);

// for ( elements in names)
// {
//     console.log(elements);
// }

// console.log(typeof(listItems));


// const ln = names.length;

const childPython = spawn( 'python', [ 'test2.py' ] );




// const childPython = spawn( 'python', [ 'code.py' ,img] );
// const childPython = spawn( 'python', [ 'test.py' ] );



childPython.stdout.on( 'data', ( data  ) =>
{
    console.log( `OUTPUT : ${data}` );
} )

childPython.stderr.on( 'data', ( data ) =>
{
    console.log( `ERROR : ${data}` );
} )