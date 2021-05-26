<?php
use App\Mascota;
use Illuminate\Http\Request;
use Illuminate\Support\Str;
use Illuminate\Support\Facades\Auth;
use Illuminate\Support\Facades\Validator;

/*
|--------------------------------------------------------------------------
| Web Routes
|--------------------------------------------------------------------------
|
| Here is where you can register web routes for your application. These
| routes are loaded by the RouteServiceProvider within a group which
| contains the "web" middleware group. Now create something great!
|
*/

Route::get('/', function () {
    return view('welcome');
});


//Route::post('/registro','API\mascotas@registro');

Route::get('/hola', function () {
    return 'hello';
});


Route::post('/reg', function (Request $request) {
    $pet=new \App\Mascota();
        $pet->nombre=$request->nombre;
        $pet->edad=$request->edad;

        if($pet->save())
{
    return response()->json($pet,200);

  
  
    
}


return response()->json(null,204);
});


Route::get('/todas', function () {

      // return allusers
      $pet= Mascota::all();
      return $pet;
  
});


