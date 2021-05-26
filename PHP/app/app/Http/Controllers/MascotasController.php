<?php

namespace App\Http\Controllers;
namespace App\Http\Controllers\API;
use App\Mascota;
use Illuminate\Http\Request;
use Illuminate\Support\Str;
use Illuminate\Support\Facades\Auth;
use Illuminate\Support\Facades\Validator;


class MascotasController extends Controller
{
    //
    public function registro(Request $request)

    {
        $pet=new \App\Mascota();
        $pet->nombre=$request->nombre;
        $pet->edad=$request->edad;

        if($pet->save())
{
    return response()->json($pet,200);

  
  
    
}


return response()->json(null,204);

    }



    public function Allmascotas()
    {
        // return allusers
        $pet= Mascota::all();
        return $pet;
                    // test succesful

    }
}
