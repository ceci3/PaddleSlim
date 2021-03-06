# Copyright (c) 2019  PaddlePaddle Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import absolute_import
from .pruner import *
from ..prune import pruner
from .auto_pruner import *
import auto_pruner
from .sensitive_pruner import *
from ..prune import sensitive_pruner
from .sensitive import *
from ..prune import sensitive
from .prune_walker import *
from ..prune import prune_walker
from io import *
from ..prune import io

__all__ = []

__all__ += pruner.__all__
__all__ += auto_pruner.__all__
__all__ += sensitive_pruner.__all__
__all__ += sensitive.__all__
__all__ += prune_walker.__all__
__all__ += io.__all__
