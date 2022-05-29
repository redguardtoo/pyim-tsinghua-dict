;;; pyim-tsinghua-dict.el --- tsinghua pinyin (quanpin) dict for pyim.

;; Copyright (C) 2021 Chen Bin <chenbin.sh@gmail.com>

;; Author: Chen Bin <chenbin.sh@gmail.com>
;; URL: https://github.com/redguardtoo/pyim-tsinghua-dict
;; Version: 0.0.1
;; Package-Requires: ((pyim "3.7"))
;; Keywords: convenience, Chinese, pinyin, input-method, complete

;;; License:

;; This file is not part of GNU Emacs.

;; This program is free software; you can redistribute it and/or
;; modify it under the terms of the GNU General Public License
;; as published by the Free Software Foundation; either version 3
;; of the License, or (at your option) any later version.

;; This program is distributed in the hope that it will be useful,
;; but WITHOUT ANY WARRANTY; without even the implied warranty of
;; MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
;; GNU General Public License for more details.

;; You should have received a copy of the GNU General Public License
;; along with GNU Emacs; see the file COPYING.  If not, write to the
;; Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor,
;; Boston, MA 02110-1301, USA.

;;; Commentary:

;; Please read README.org.

;;; Code:
(require 'pyim-dict)

;;;###autoload
(defun pyim-tsinghua-dict-enable ()
  "Add tsinghua dict to pyim."
  (interactive)
  (let* ((dir (file-name-directory
               (locate-library "pyim-tsinghua-dict.el")))
         (file (concat dir "pyim-tsinghua-dict.pyim")))
    (when (file-exists-p file)
      (if (featurep 'pyim-dict)
          (pyim-extra-dicts-add-dict
           `(:name "tsinghua-dict-elpa" :file ,file :elpa t))
        (message "pyim 没有安装，pyim-tsinghua-dict 启用失败。")))))

(provide 'pyim-tsinghua-dict)

;;; pyim-tsinghua-dict.el ends here
