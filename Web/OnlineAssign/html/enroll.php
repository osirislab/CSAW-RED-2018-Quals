<?php
require_once 'auth.php';
require_once 'models.php';

$u = get_user();

if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    die("Method not allowed");
}

if (!isset($_POST['course'])) {
    die("Must specify course to enroll in");
}

$course = Course::withID($_POST['course']);

if ($course == null) {
    http_response_code(404);
    die();
}

$course->enroll($u);

header('Location: course.php?id=' . $course->id);
