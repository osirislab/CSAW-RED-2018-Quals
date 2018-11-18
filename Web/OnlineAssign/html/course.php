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

$assignments = $course->assignments();
include 'header.php';
?>
        <div class="content">
            <div>
                <h3><?php echo $course->name; ?></h3>
            </div>

            <div class="panel">
                <h4>Open Assignments</h4>
                <?php foreach ($assignments as $a) { if ($a->isOpen()) { ?>
                    <a href="assignment.php?id=<?php echo $a->id; ?>"><?php echo $a->name; ?></a>
                <?php }} ?>
                <h4>Past Assignments</h4>
                <?php foreach ($assignments as $a) { if (!$a->isOpen()) { ?>
                    <a href="assignment.php?id=<?php echo $a->id; ?>"><?php echo $a->name; ?></a>
                <?php }} ?>
            </div>
        </div>
<?php
include 'footer.php';
?>
