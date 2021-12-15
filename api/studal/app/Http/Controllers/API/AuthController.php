<?php

namespace App\Http\Controllers\API;

use Illuminate\Http\Request;
use App\Http\Controllers\API\MainController as MainController;
use Illuminate\Support\Facades\Auth;
use Validator;
use App\Models\User;

class AuthController extends MainController {

    public function signin( Request $request ) {

        if( Auth::attempt([ "name" => $request->name, "password" => $request->password ])) {

            $authUser = Auth::user();
            $success[ "token" ] = $authUser->createToken( "MyAuthApp" )->plainTextToken;
            $success[ "name" ] = $authUser->name;
        
            return $this->sendResponse( $success, "User signed in" );

        }else {

            return $this->sendError( "Unauthorized", [ "error" => "Unauthorized" ]);
        }
    }

    public function signup( Request $request ) {

        $validator = Validator::make( $request->all(), [
            "name" => "required",
            "email" => "required",
            "password" => "required",
            "confirm_password" => "required|same:password"
        ]);

        if( $validator->fails() ) {

            return $this->sendError( "Error validation", $validator->errors() );
        }

        $input = $request->all();
        $input[ "password" ] = bcrypt( $input[ "password" ]);
        $user = User::create( $input );
        $success[ "token" ] = $user->createToken( "MyAuthApp" )->plainTextToken;
        $success[ "name" ] = $user->name;

        return $this->sendResponse( $success, "User created successfully" );
    }
}