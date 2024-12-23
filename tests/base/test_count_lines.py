# -*- coding: utf-8 -*-
from tests.helpers import data
from biomodules.base.count_lines import CountLines


class TestCountLines:
    def test_without_comment_char(self):
        assert CountLines(data('ref.fa'))() == 2388

    def test_with_comment_char(self):
        assert CountLines(data('ref.fa'), '>')() == 2189
