# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

try:
    from ._models_py3 import ErrorFieldContract
    from ._models_py3 import WorkbookError, WorkbookErrorException
    from ._models_py3 import WorkbookTemplate
    from ._models_py3 import WorkbookTemplateGallery
    from ._models_py3 import WorkbookTemplateLocalizedGallery
    from ._models_py3 import WorkbookTemplateResource
    from ._models_py3 import WorkbookTemplateUpdateParameters
except (SyntaxError, ImportError):
    from ._models import ErrorFieldContract
    from ._models import WorkbookError, WorkbookErrorException
    from ._models import WorkbookTemplate
    from ._models import WorkbookTemplateGallery
    from ._models import WorkbookTemplateLocalizedGallery
    from ._models import WorkbookTemplateResource
    from ._models import WorkbookTemplateUpdateParameters
from ._paged_models import WorkbookTemplatePaged

__all__ = [
    'ErrorFieldContract',
    'WorkbookError', 'WorkbookErrorException',
    'WorkbookTemplate',
    'WorkbookTemplateGallery',
    'WorkbookTemplateLocalizedGallery',
    'WorkbookTemplateResource',
    'WorkbookTemplateUpdateParameters',
    'WorkbookTemplatePaged',
]
