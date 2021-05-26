<?php

use Illuminate\Http\Request;

/*
|--------------------------------------------------------------------------
| API Routes
|--------------------------------------------------------------------------
|
| Here is where you can register API routes for your application. These
| routes are loaded by the RouteServiceProvider within a group which
| is assigned the "api" middleware group. Enjoy building your API!
|
*/

Route::middleware('auth:api')->get('/user', function (Request $request) {
    return $request->user();
});

#Route::post('/registro','API\mascotas@registro');

Route::post('/registro','MascotasController@registro');
Route::get('/all','MascotasController@Allmascotas');



#Route::resource('registro', 'API\MascotasController@registro');

#Route::post('/registro', 'API\MascotasController@registro')->name('registro');
