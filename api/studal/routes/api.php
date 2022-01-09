<?php

use Illuminate\Http\Request;
use Illuminate\Support\Facades\Route;
use App\Http\Controllers\StudentController;
use App\Http\Controllers\AuthController;
use App\Http\Controllers\ClassGroupController;

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
    Route::post( "/logout", [ AuthController::class, "logout" ]);
    
    Route::post( "/students", [ StudentController::class, "store" ]);
    Route::put( "/students/{id}", [ StudentController::class, "update" ]);
    Route::delete( "/students/{id}", [ StudentController::class, "destroy" ]);

    Route::post( "/groups", [ ClassGroupController::class, "store" ]);
    Route::put( "/groups/{id}", [ ClassGroupController::class, "update" ]);
    Route::delete( "/groups/{id}", [ ClassGroupController::class, "destroy" ]);
});

Route::post( "/register", [ AuthController::class, "register" ]);
Route::post( "/login", [ AuthController::class, "login" ]);

Route::get( "/students/groups/{id}", [ StudentController::class, "index" ]);
Route::get( "/students/{id}", [ StudentController::class, "show" ]);
Route::get( "/students/search/{name}", [ StudentController::class, "search" ]);

Route::get( "/groups", [ ClassGroupController::class, "index" ]);