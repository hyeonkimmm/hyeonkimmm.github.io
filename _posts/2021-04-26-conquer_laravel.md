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
<?php

namespace App\Console;

use Illuminate\Console\Scheduling\Schedule;
use Illuminate\Foundation\Console\Kernel as ConsoleKernel;
use Illuminate\Support\Facades\DB;

class Kernel extends ConsoleKernel
{
    /**
     * The Artisan commands provided by your application.
     *
     * @var array
     */
    protected $commands = [
        //
    ];

    /**
     * Define the application's command schedule.
     *
     * @param  \Illuminate\Console\Scheduling\Schedule  $schedule
     * @return void
     */
    protected function schedule(Schedule $schedule)
    {
        $schedule->call(function () {
            DB::table('recent_users')->delete();
        })->daily();
    }
}
```
In addition to scheduling using Closures, you may also use invokable objects. Invokable objects are simple PHP classes that contain an `__invoke method:`
호출 불가능한 객체도 `__invoke` method에서 불러올 수 있음.
```php
$schedule->call(new DeleteRecentUsers)->daily();
```
#### Scheduling Artisan Commands
In addition to scheduling Closure calls, you may also schedule [Artisan commands](https://laravel.com/docs/6.x/artisan) and operating system commands. For example, you may use the `command` method to schedule an Artisan command using either the command's name or class:

closure 스케줄링을 호출하는 것 외에도 artisan commands과 운영체제 명령을 실행하는 스케줄링도 가능하다. 예를들어 command method에 아래와 같이 작성한다.
```php
$schedule->command('emails:send Taylor --force')->daily();

$schedule->command(EmailsCommand::class, ['Taylor', '--force'])->daily();
```
#### Scheduling Queued Jobs
The `job` method may be used to schedule a queued job. This method provides a convenient way to schedule jobs without using the call method to manually create Closures to queue the job:
```php
$schedule->job(new Heartbeat)->everyFiveMinutes();

// Dispatch the job to the "heartbeats" queue...
$schedule->job(new Heartbeat, 'heartbeats')->everyFiveMinutes();
```
job method를 활용해서 예약된 job을 실행 할 수 있다. call method를 실행하지 않고도 가능

#### Scheduling Shell Commands
The `exec` method may be used to issue a command to the operating system:
```php
$schedule->exec('node /home/forge/script.js')->daily();
```

#### Schedule Frequency Options
There are a variety of schedules you may assign to your task:

These methods may be combined with additional constraints to create even more finely tuned schedules that only run on certain days of the week. For example, to schedule a command to run weekly on Monday:
```php
// Run once per week on Monday at 1 PM...
$schedule->call(function () {
    //
})->weekly()->mondays()->at('13:00');

// Run hourly from 8 AM to 5 PM on weekdays...
$schedule->command('foo')
          ->weekdays()
          ->hourly()
          ->timezone('America/Chicago')
          ->between('8:00', '17:00');
```
**Between Time Constraints**
The `between` method may be used to limit the execution of a task based on the time of day:
```php
$schedule->command('reminders:send')
                    ->hourly()
                    ->between('7:00', '22:00');
```
Similarly, the `unlessBetween` method can be used to exclude the execution of a task for a period of time:
```php
$schedule->command('reminders:send')
                    ->hourly()
                    ->unlessBetween('23:00', '4:00');
```
unlessBetween을 통해 이시간동안 task를 실행하지 않게 진행할 수 있음.

**Truth Test Constraints**
The `when` method may be used to limit the execution of a task based on the result of a given truth test. In other words, if the given `Closure` returns `true`, the task will execute as long as no other constraining conditions prevent the task from running:

```php
$schedule->command('emails:send')->daily()->when(function () {
    return true;
});
```
When using chained `when` methods, the scheduled command will only execute if all `when` conditions return `true`.

**Environment Constraints**
The `environments` method may be used to execute tasks only on the given environments:
```php
$schedule->command('emails:send')
            ->daily()
            ->environments(['staging', 'production']);
```
### Timezones
Using the `timezone` method, you may specify that a scheduled task's time should be interpreted within a given timezone:
```php
$schedule->command('report:generate')
         ->timezone('America/New_York')
         ->at('02:00')
```
timezone method를 활용하면 지역별 시간대에 맞게 특정하여 scheduled할 수 있음
