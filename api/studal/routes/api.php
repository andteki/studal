<?php

use Illuminate\Http\Request;
use Illuminate\Support\Facades\Route;
use App\Http\Controllers\StudentController;
use App\Http\Controllers\AuthController;

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

Route::group([ "middleware" => [ "auth:sanctum" ]], function () {
    Route::post( "/students", [ StudentController::class, "store" ]);
    Route::put( "/students/{id}", [ StudentController::class, "update" ]);
    Route::delete( "/students/{id}", [ StudentController::class, "destroy" ]);
});

Route::post( "/register", [ AuthController::class, "register" ]);
Route::post( "/login", [ AuthController::class, "login" ]);
Route::post( "/logout", [ AuthController::class, "logout" ]);
Route::get( "/students", [ StudentController::class, "index" ]);
Route::get( "/students/{id}", [ StudentController::class, "show" ]);
Route::get( "/students/search/{name}", [ StudentController::class, "search" ]);