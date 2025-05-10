# -*- coding: utf-8 -*-
from pathlib import Path
from tempfile import TemporaryDirectory

from Bio import SeqIO

from tests.helpers import data
from biomodules.seq.subseq import SubSeq


def test_subseq():
    infile = data('ref.fa')
    with TemporaryDirectory() as tempdir:
        outfile = Path(tempdir) / 'seqs.fa'
        SubSeq(
            infile=infile,
            ids=['1', '2'],
            outfile=outfile,
            extra='>3\nATCG\n'
        )()
        id2seq = {seq.id: seq for seq in SeqIO.parse(outfile, 'fasta')}
        assert len(id2seq) == 3
        assert '1' in id2seq
        assert '2' in id2seq
        assert '3' in id2seq
        assert str(id2seq['3'].seq) == 'ATCG'
