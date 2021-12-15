<?php

use Illuminate\Http\Request;
use Illuminate\Support\Facades\Route;
use App\Http\Controllers\API\AuthController;
use App\Http\Controllers\API\StudentController;

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
Route::post( "login", [ AuthController::class, "signin" ]);
Route::post( "register", [ AuthController::class, "signup" ]);
Route::get( "students", [ StudentController::class, "index" ]);
Route::post( "students", [ StudentController::class, "store" ]);
Route::get( "students/{student}", [ StudentControoler::class, "show" ]);
Route::put( "students/{student}", [ StudentController::class, "update" ]);
Route::delete( "students/{student}", [ StudentController::class, "destroy" ]);

Route::middleware('auth:sanctum')->get('/user', function (Request $request) {
    return $request->user();
});


