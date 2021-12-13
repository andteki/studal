<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

class CreateStudentsTable extends Migration
{
    /**
     * Run the migrations.
     *
     * @return void
     */
    public function up() {

        Schema::create( 'students', function( Blueprint $table ) {
            $table->increments( "sid" );
            $table->string( "name", 100 );
            $table->string( "email", 100 );
            $table->string( "phone", 9 );
            $table->date( "borndate" );
            $table->integer( "classgroupid" )->unsigned();
            $table->foreign( "classgroupid" )->references( "cgid" )->on( "classgroups" );
            $table->timestamps();
        });
    }

    /**
     * Reverse the migrations.
     *
     * @return void
     */
    public function down() {

        Schema::dropIfExists('students');
    }
}
