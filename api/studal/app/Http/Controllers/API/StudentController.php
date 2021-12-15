<?php

namespace App\Http\Controllers\API;

use Illuminate\http\Request;
use App\Http\Controllers\API\MainController as MainController;
use Validator;
use App\Models\Student;
use App\Http\Resources\Student as StudentResource;

class StudentController extends MainController {

    public function index() {

        $students = Student::all();

        return $this->sendResponse( StudentResource::collection( $students ), "Students fetched" );
    }

    public function store( Request $request ) {

        $input = $request->all();
        $validator = Validator::make( $input, [
            "name" => "required",
            "email" => "required",
            "phone" => "required",
            "borndate" => "required"
        ]);

        if( $validator->fails() ) {

            return $this->sendError( $validator->errors() );
        }

        $student = Student::create( $input );

        return $this->sendResponse( new StudentResource( $student ), "Student created" );
    }

    public function show( $name ) {

        $student = Student::find( $name );

        if( is_null( $student )) {

            return $this->sendError( "Class does not exists" );
        }

        return $this->sendResponse( new StudentResource( $student ), "Students fetched" );
    }

    public function update( Request $request, Student $student ) {

        $input = $request->all();
        $validator = Validator::make( $input, [
            "name" => "required",
            "email" => "required",
            "phone" => "required",
            "borndate" => "required",
        ]);

        if( $validator->fails() ) {

            return $this->sendError( $validator->errors() );
        }

        $student->name = $input[ "name" ];
        $student->email = $input[ "email" ];
        $student->phone = $input[ "phone" ];
        $student-> borndate = $input[ "borndate" ];
        $student->save();

        return $this->sendResponse( new StudentResource( $student ), "Student updated" );
    }

    public function destroy( Student $student ) {

        $student->delete();

        return $this->sendResponse( [], "Student deleted" );
    }
}