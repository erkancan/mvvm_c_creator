//
//  ___FILENAME___
//  ___PROJECTNAME___
//
//  Created by ___FULLUSERNAME___ on ___DATE___.
//  Copyright (c) ___YEAR___ ___ORGANIZATIONNAME___. All rights reserved.
//

import UIKit

enum ___VARIABLE_sceneName___Route {

}

protocol ___VARIABLE_sceneName___CoordinatorDelegate: class {
    func coordinator(_ coordinator: ___VARIABLE_sceneName___Coordinator, finishedWithSuccess success: Bool)
}

protocol ___VARIABLE_sceneName___CoordinatorProtocol {
    func navigate(to route: ___VARIABLE_sceneName___Route)
}

final class ___VARIABLE_sceneName___Coordinator: Coordinator {
    
    // MARK: - Properties
    private let navigationController: UINavigationController
    weak var delegate: ___VARIABLE_sceneName___CoordinatorDelegate?

    internal var children: [Coordinator]

    // MARK: - Lifecycle
    init(navigationController: UINavigationController) {
        self.navigationController = navigationController
        children = []
    }

    // MARK: - Methods
    func start() {
        let viewModel: ___VARIABLE_sceneName___ViewModelProtocol = ___VARIABLE_sceneName___ViewModel(coordinator: self)
        let viewController = ___VARIABLE_sceneName___ViewController(viewModel: viewModel)

        // FIXME: Display as you need
        // navigationController.setViewControllers([viewController], animated: false)
    }
}

extension ___VARIABLE_sceneName___Coordinator: ___VARIABLE_sceneName___CoordinatorProtocol {
    func navigate(to route: ___VARIABLE_sceneName___Route) {
        
    }
}
