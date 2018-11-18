<?php
require_once 'auth.php';

$u = get_user();

if (!isset($_REQUEST['id'])) {
    die("Missing id");
}

$course = Course::withID($_GET['id']);

if ($course == null) {
    http_response_code(404);
    die();
}

if ($course->instructor()->id !== $u->id) {
    http_response_code(403);
    die();
}

$assignments = $course->assignments();
include 'header.php';
?>
        <div class="content">
            <div>
                <h3><?php echo $course->name; ?></h3>
            </div>

            <div class="panel">
                <h4>Students</h4>
                <?php foreach ($course->students() as $s) { ?>
                    <p><?php echo $s->realname; ?></p>
                <?php } ?>
            </div>

            <div class="panel">
                <h4>Assignments</h4>
                <?php foreach ($assignments as $a) { ?>
                    <p><a href="manage_assignment.php?id=<?php echo $a->id; ?>"><?php echo $a->name; ?></a></p>
                <?php } ?>
            </div>
        </div>
<?php
include 'footer.php';
?>
