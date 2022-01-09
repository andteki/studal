<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Models\Classgroup;

class ClassGroupController extends Controller
{
    public function index() {

        return Classgroup::all();
    }

    public function store( Request $request ) {

        return Classgroup::create( $request->all() );
    }

    public function update( Request $request, $id ) { 
        
        $classgroup = Classgroup::find( $id );
        $classgroup->update( $request->all() );
        return $classgroup;
    }

    public function destroy( $id ){

        return Classgroup::destroy( $id );
    }
}
