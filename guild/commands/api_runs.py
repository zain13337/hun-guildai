# Copyright 2017-2022 RStudio, PBC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import absolute_import
from __future__ import division

import json

import click

from guild import click_util

from . import runs_support


@click.command("runs")
@click.option("-f", "--format", is_flag=True, help="Format the JSON outout.")
@runs_support.runs_arg
@runs_support.all_filters
@click_util.use_args
@click.option("--include-batch", is_flag=True, help="Include batch runs.")
@click_util.render_doc
def main(args):
    """Show runs as JSON."""
    print(_encode_data(_runs_data(args), args))


def _runs_data(args):
    from .view_impl import ViewDataImpl

    return ViewDataImpl(args).runs_data()


def _encode_data(data, args):
    json_opts = {"indent": 2, "sort_keys": True} if args.format else {}
    return json.dumps(data, **json_opts)
