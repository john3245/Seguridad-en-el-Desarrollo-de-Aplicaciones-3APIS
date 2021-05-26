<?php

namespace App\Http\Controllers;
use App\Mascota;

use Illuminate\Http\Request;

class mascotas extends Controller
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
}
