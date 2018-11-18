<?php

require_once 'db.php';

class User {
    public $id, $username, $realname;

    public static function fromArray($arr) {
        $u = new User;
        $u->id = $arr['id'];
        $u->username = $arr['username'];
        $u->realname = $arr['realname'];

        return $u;
    }

    public static function withID($id) {
        $a = DB::queryDB("SELECT * FROM user WHERE id = :id", array(":id" => $id), 1);
        if ($a && count($a) == 1) {
            return self::fromArray($a[0]);
        } else {
            return null;
        }
    }

    public static function login($username, $password) {
        $a = DB::queryDB(
            "SELECT * FROM user WHERE username = :username AND password = :hashpass",
            array(":username" => $username, ":hashpass" => hash('sha256', $password, true)),
            1);
        if ($a && count($a) == 1) {
            return self::fromArray($a[0]);
        } else {
            return null;
        }
    }

    public static function register($username, $realname, $password) {
        $id = DB::queryDB(
            "INSERT INTO user (username, realname, password) VALUES (:username, :realname, :hashpass)",
            array(":username" => $username, ":realname" => $realname, ":hashpass" => hash('sha256', $password, true)),
            0);
        if ($id !== false) {
            return self::withID($id);
        } else {
            return null;
        }
    }

    public function enrolledCourses() {
        $coursesArr = DB::queryDB(
            "SELECT * FROM course INNER JOIN enrollment ON enrollment.course_id = course.id WHERE enrollment.user_id = :id OR course.instructor_id = :id",
            array(":id" => $this->id),
            -1);
        return array_map("Course::fromArray", $coursesArr);
    }
}

class Course {
    private $instructor_id;
    public $id, $name;

    public static function fromArray($arr) {
        $c = new Course;
        $c->id = $arr['id'];
        $c->name = $arr['name'];
        $c->instructor_id = $arr['instructor_id'];

        return $c;
    }

    public static function withID($id) {
        $a = DB::queryDB("SELECT * FROM course WHERE id = :id", array(":id" => $id), 1);
        if ($a && count($a) == 1) {
            return self::fromArray($a[0]);
        } else {
            return null;
        }
    }

    public static function allCourses() {
        $a = DB::queryDB("SELECT * FROM course", array(), -1);
        return array_map("Course::fromArray", $a);
    }

    public function assignments() {
        $assignmentsArr = DB::queryDB(
            "SELECT * FROM assignment WHERE course_id = :id AND open_date <= NOW()",
            array(":id" => $this->id),
            -1);
        return array_map("Assignment::fromArray", $assignmentsArr );
    }

    public function instructor() {
        return User::withID($this->instructor_id);
    }

    public function enroll($u) {
        $i = DB::queryDB("INSERT INTO enrollment VALUES (:cid, :uid)", array(":cid" => $this->id, ":uid" => $u->id), 0);
        return $i;
    }

    public function students() {
        $a = DB::queryDB("SELECT * FROM user INNER JOIN enrollment ON enrollment.user_id = user.id WHERE enrollment.course_id = :id", array(":id" => $this->id), -1);
        return array_map("User::fromArray", $a);
    }
}

class Assignment {
    private $course_id;
    public $id, $open_date, $due_date, $name;

    public static function fromArray($arr) {
        $a = new Assignment;
        $a->id = $arr['id'];
        $a->course_id = $arr['course_id'];
        $a->open_date = $arr['open_date'];
        $a->due_date = $arr['due_date'];
        $a->name = $arr['name'];
        return $a;
    }

    public static function withID($id) {
        $a = DB::queryDB("SELECT * FROM assignment WHERE id = :id", array(":id" => $id), 1);
        if ($a && count($a) == 1) {
            return self::fromArray($a[0]);
        } else {
            return null;
        }
    }

    public function course() {
        return Course::withID($this->course_id);
    }

    public function questions() {
        $qsArr = DB::queryDB("SELECT * FROM question WHERE assignment_id = :id", array(":id" => $this->id), -1);
        return array_map("Question::fromArray", $qsArr);
    }

    public function isOpen() {
        return strtotime($this->open_date) <= time() && strtotime($this->due_date) > time();
    }
}
        
class Question {
    public $id, $name, $body, $checker;

    public static function fromArray($arr) {
        $q = new Question;
        $q->id = $arr['id'];
        $q->name = $arr['name'];
        $q->body = $arr['body'];
        $q->checker = $arr['checker'];
        return $q;
    }

    public static function withID($id) {
        $a = DB::queryDB("SELECT * FROM question WHERE id = :id", array(":id" => $id), 1);
        if ($a && count($a) == 1) {
            return self::fromArray($a[0]);
        } else {
            return null;
        }
    }
}

class Message {
    private $student_id, $instructor_id, $question_id, $assignment_id;
    public $id, $message;

    public static function fromArray($arr) {
        $m = new Message;
        $m->id = $arr['id'];
        $m->student_id = $arr['student_id'];
        $m->instructor_id = $arr['instructor_id'];
        $m->question_id = $arr['question_id'];
        $m->assignment_id = $arr['assignment_id'];
        $m->message = $arr['message'];
        return $m;
    }

    public static function withID($id) {
        $a = DB::queryDB("SELECT * FROM message WHERE id = :id", array(":id" => $id), 1);
        if ($a && count($a) == 1) {
            return self::fromArray($a[0]);
        } else {
            return null;
        }
    }

    public static function send($from, $to, $question, $assignment, $msg) {
        $msg_id = DB::queryDB(
            "INSERT INTO message (student_id, instructor_id, question_id, assignment_id, message) VALUES (:sid, :tid, :qid, :aid, :msg)",
            array(":sid" => $from->id, ":tid" => $to->id, ":qid" => $question->id, ":aid" => $assignment->id, ":msg" => $msg),
            0);
        return $msg_id;
    }

    public function student() {
        return User::withID($this->student_id);
    }

    public function question() {
        return Question::withID($this->question_id);
    }

    public function assignment() {
        return Assignment::withID($this->assignment_id);
    }
}
