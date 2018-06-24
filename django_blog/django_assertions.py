from django.test import TestCase

_dj_testcase = TestCase()

dj_assert_contains = _dj_testcase.assertContains
dj_assert_not_contains = _dj_testcase.assertNotContains
dj_assert_template_used = _dj_testcase.assertTemplateUsed
dj_assert_subtest = _dj_testcase.subTest