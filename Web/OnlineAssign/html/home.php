<?php
require_once 'auth.php';
require_once 'models.php';

$u = get_user();
$userCourses = $u->enrolledCourses();
$allCourses = Course::allCourses();

include 'header.php';
?>
        <div class="content">
            <div>
                <h2>Home</h2>
                <h3><?php echo $u->realname; ?></h3>
            </div>
            <p><?php if ($u->id == 2) { echo file_get_contents("/var/www/flag2.txt"); } ?></p>
            <div class="panel">
                <h4>My Classes</h4>
                <?php foreach ($userCourses as $c) { ?>
                    <?php if ($c->instructor()->id === $u->id) { ?>
                    <p><a href="manage_course.php?id=<?php echo $c->id; ?>"><?php echo $c->name; ?></a></p>
                    <?php } else { ?>
                    <p><a href="course.php?id=<?php echo $c->id; ?>"><?php echo $c->name; ?></a></p>
                    <?php } ?>
                <?php } ?>
                <form action="enroll.php" method="POST">
                    <select name="course">
                    <?php foreach ($allCourses as $c) { ?>
                        <option value="<?php echo $c->id; ?>"><?php echo $c->name; ?></option>
                    <?php } ?>
                    <input type="submit" value="Enroll" />
                </form>
            </div>
            <div class="panel">
                <h4>Open Assignments</h4>
                <?php foreach ($userCourses as $c) { if ($c->instructor()->id !== $u->id) { foreach ($c->assignments() as $a) { ?>
                    <a href="assignment.php?id=<?php echo $a->id; ?>"><?php echo $a->name; ?></a>
                <?php }}} ?>
            </div>
        </div>
<?php
include 'footer.php';
?>
