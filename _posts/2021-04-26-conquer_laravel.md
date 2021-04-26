---
title : "Laravel Documentation - Task Scheduling"
category :
    - PHP
    - Laravel
tag :
    - Laravel
    - Task Scheduling
toc : true
---
- PHP Laravel documentation 을 읽고 정리한 글.
- Laravel 최신 LTS인 6.X 버전의 Documentation.
## [Task Scheduling](https://laravel.com/docs/6.x/scheduling#introduction)
### Introduction
In the past, you may have generated a Cron entry for each task you needed to schedule on your server. However, this can quickly become a pain, because your task schedule is no longer in source control and you must SSH into your server to add additional Cron entries.

작업 스케줄링 할 때, cron을 source control 부분에서 사용하지 않고 서버에 SSH를 입력해서 cron 항목을 추가해야 한다.
- 참고: Cron 유닉스 계열 컴퓨터 운영 체제의 시간 기반 잡 스케줄러이다

Laravel's command scheduler allows you to fluently and expressively define your command schedule within Laravel itself. When using the scheduler, only a single Cron entry is needed on your server. Your task schedule is defined in the `app/Console/Kernel.php` file's `schedule` method. To help you get started, a simple example is defined within the method.
라라벨의 명령 스케줄러는 라라벨 내에서 명령 스케줄을 유창하고 표현적으로 정의할 수 있게 해준다.
스케줄러를 사용할 때 서버에서는 오직 하나의 cron만 필요함.
너의 테스크 스케줄은 kernel.php 파일의 schedule method에 정의되어 있다.
간단한 example이 method 내에 정의되어 있다.


#### Starting The Scheduler
When using the scheduler, you only need to add the following Cron entry to your server. If you do not know how to add Cron entries to your server, consider using a service such as [Laravel Forge](https://forge.laravel.com/) which can manage the Cron entries for you:

스케쥴러를 사용할때 cron entry를 너의 서버에 추가해주면 된다.
모르면 laravel forge와 같은 서비스를 이용해봐라

```php
* * * * * cd /path-to-your-project && php artisan schedule:run >> /dev/null 2>&1
```
This Cron will call the Laravel command scheduler every minute. When the `schedule:run` command is executed, Laravel will evaluate your scheduled tasks and runs the tasks that are due.

이 크론은 laravel 명령 스케쥴러를 매분마다 호출한다. `schedule:run` 명령이 실행되면 laravel은 너가 설정한 예정된 작업을 평가하고 실행할 것이다.

### Defining Schedules
You may define all of your scheduled tasks in the `schedule` method of the `App\Console\Kernel` class. To get started, let's look at an example of scheduling a task. In this example, we will schedule a `Closure` to be called every day at midnight. Within the `Closure` we will execute a database query to clear a table:

`App\Console\Kernel` class에 `schedule` method에서 scheduled task를 정의 할 수 있습니다. a task라는 예시를 통해 시작합니다.
우리는 `Closure`를 매일 자정에 호출할 것이다.
`Closure`안에 있는 table을 비우기 위해 database query를 실행할 것 입니다.

```php
<?php  namespace App\Console;  use 
Illuminate\Console\Scheduling\Schedule; use 
Illuminate\Foundation\Console\Kernel as ConsoleKernel; use 
Illuminate\Support\Facades\DB;  
class Kernel extends ConsoleKernel {
    /**      
    * The Artisan commands provided by your application.      *
          * @var array      */     
          protected $commands = [         //     ];      
          /**      
          * Define the application's command schedule.      *      * @param  \Illuminate\Console\Scheduling\Schedule  $schedule      * @return void      */     
          protected function schedule(Schedule $schedule)     {         $schedule->call(function () {             DB::table('recent_users')->delete();         })->daily();     } }
```
