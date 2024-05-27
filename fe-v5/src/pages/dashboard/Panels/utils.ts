/*
 * Copyright 2022 Nightingale Team
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 *
 */
import _ from 'lodash';
import { IPanel } from '../types';
import { JSONParse } from '../utils';

export function buildLayout(panels: IPanel[]) {
  return _.map(panels, (item: IPanel) => {
    return {
      ...item.layout,
      i: _.toString(item.layout.i),
      isResizable: item.type !== 'row',
    };
  });
}

export function sortPanelsByGridLayout(panels: IPanel[]) {
  return panels.sort((panelA, panelB) => {
    if (panelA.layout.y === panelB.layout.y) {
      return panelA.layout.x - panelB.layout.x;
    } else {
      return panelA.layout.y - panelB.layout.y;
    }
  });
}

export function updatePanelsLayout(panels: IPanel[], newLayout: IPanel) {
  return _.map(panels, (panel: IPanel) => {
    const newPanel = { ...panel };
    const findedLayout = _.find(newLayout, { i: newPanel.layout.i });
    if (findedLayout) {
      // newLayout 可能是 ReactGridLayout.onLayoutChange 中的参数，掺杂了其他属性
      newPanel.layout = _.pick(findedLayout, ['h', 'w', 'x', 'y', 'i', 'isResizable']);
    }
    return newPanel;
  });
}

export function getRowIndex(panels: IPanel[], id: string) {
  return _.findIndex(panels, { id });
}

export function getRowPanels(panels: IPanel[], rowId: string): IPanel[] {
  const rowIndex = getRowIndex(panels, rowId);
  const rowPanels: IPanel[] = [];
  for (let index = rowIndex + 1; index < panels.length; index++) {
    const panel = panels[index];
    if (panel.type === 'row') {
      break;
    }
    rowPanels.push(panel);
  }
  return rowPanels;
}

export function getNextRow(panels: IPanel[], rowId: string): IPanel | undefined {
  const rowIndex = getRowIndex(panels, rowId);
  let row: IPanel | undefined = undefined;
  for (let index = rowIndex + 1; index < panels.length; index++) {
    const panel = panels[index];
    if (panel.type === 'row') {
      row = panel;
      break;
    }
  }
  return row;
}

export function getRowPanelsMaxY(panels: IPanel[], rowId: string) {
  const rowPanels = getRowPanels(panels, rowId);
  const rowPanel = _.find(panels, { id: rowId });
  let maxY = rowPanel.layout.y + rowPanel.layout.h;
  _.forEach(rowPanels, (panel) => {
    if (panel.layout.y + panel.layout.h > maxY) {
      maxY = panel.layout.y + panel.layout.h;
    }
  });
  return maxY;
}
export function getRowCollapsedPanels(panels: IPanel[], row: IPanel) {
  let newPanels = _.cloneDeep(panels);
  const rowIndex = getRowIndex(newPanels, row.id);
  const cacheRowPanels = row.panels;
  if (cacheRowPanels && cacheRowPanels.length > 0) {
    const firstPanelYPos = cacheRowPanels[0].layout.y ?? row.layout.y;
    const yDiff = firstPanelYPos - (row.layout.y + row.layout.h);
    let insertPos = rowIndex + 1;
    let yMax = row.layout.y;
    for (const panel of cacheRowPanels) {
      panel.layout.y ?? (panel.layout.y = row.layout.y);
      panel.layout.y -= yDiff;
      newPanels.splice(insertPos, 0, panel);
      insertPos += 1;
      yMax = Math.max(yMax, panel.layout.y + panel.layout.h);
    }
    const pushDownAmount = yMax - row.layout.y - 1;
    for (let panelIndex = insertPos; panelIndex < newPanels.length; panelIndex++) {
      newPanels[panelIndex].layout.y += pushDownAmount;
    }
    newPanels = _.unionBy(newPanels, 'id');
    const curRow = _.find(newPanels, { id: row.id });
    curRow.panels = [];
  }
  return newPanels;
}
export function getRowUnCollapsedPanels(panels: IPanel[], row: IPanel) {
  let newPanels = _.cloneDeep(panels);
  const curRowPanels = getRowPanels(newPanels, row.id);
  if (curRowPanels.length > 0) {
    newPanels = _.filter(newPanels, (panel) => {
      return !_.find(curRowPanels, { id: panel.id });
    });
    const curRow = _.find(newPanels, { id: row.id });
    curRow.panels = curRowPanels;
  }
  return newPanels;
}
/**
 * 处理 Row 组件切换时需要更新的 panels，返回更新后的 panels
 * 关闭 row 时，需要把 row 下面的 rowPanels 删除掉，并且缓存被删除的 panels
 * 展开 row 是，需要把 row 下面的缓存的 rowPanels 添加到 panels 中
 */
export function handleRowToggle(collapsed, panels: IPanel[], row: IPanel): IPanel[] {
  let newPanels = _.cloneDeep(panels);
  if (collapsed) {
    newPanels = getRowCollapsedPanels(newPanels, row);
  } else {
    newPanels = getRowUnCollapsedPanels(newPanels, row);
  }
  const curRow = _.find(newPanels, { id: row.id });
  curRow.collapsed = collapsed;
  return newPanels;
}

export function updatePanelsWithNewPanel(panels: IPanel[], newPanel: IPanel) {
  return _.map(panels, (panel: IPanel) => {
    if (panel.id === newPanel.id) {
      return newPanel;
    }
    return panel;
  });
}

export function updatePanelsInsertNewPanel(panels: IPanel[], newPanel: IPanel) {
  return _.concat(panels, newPanel);
}

// 新增面板的宽高初始值
const PANEL_W = 12;
const PANEL_H = 4;

// 新增 panel 到全局
export function updatePanelsInsertNewPanelToGlobal(panels: IPanel[], panel: any, type: 'row' | 'chart') {
  const w = type === 'row' ? 24 : PANEL_W;
  const h = type === 'row' ? 1 : PANEL_H;
  const maxItem = _.maxBy(panels, (item: IPanel) => {
    return item.layout.y + item.layout.h;
  });
  const newPanel = {
    ...panel,
    layout: {
      x: 0,
      y: maxItem ? maxItem.layout.y + maxItem.layout.h : 0,
      w,
      h,
      i: panel.id,
    },
  };
  return _.concat([...panels], newPanel);
}

// 新增 panel 到分组
export function updatePanelsInsertNewPanelToRow(panels: IPanel[], rowId: string, panel: IPanel) {
  const nextRow = getNextRow(panels, rowId);
  let nextRowIdx;
  if (nextRow?.id) {
    nextRowIdx = getRowIndex(panels, nextRow?.id);
  }
  const maxY = getRowPanelsMaxY(panels, rowId);
  const newPanel = {
    ...panel,
    layout: {
      x: 0,
      y: maxY,
      w: PANEL_W,
      h: PANEL_H,
      i: panel.id,
    },
  };
  const newPanels = _.map(panels, (item, idx) => {
    if (idx >= nextRowIdx) {
      return {
        ...item,
        layout: {
          ...item.layout,
          y: item.layout.y + PANEL_H,
        },
      };
    }
    return item;
  });
  return _.concat(newPanel, newPanels);
}

export function panelsMergeToConfigs(configs: string | undefined, panels: any[]) {
  const parsedConfigs = JSONParse(configs);
  parsedConfigs.panels = panels;
  return JSON.stringify(parsedConfigs);
}
