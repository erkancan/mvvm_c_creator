//
//  ___FILENAME___
//  ___PROJECTNAME___
//
//  Created by ___FULLUSERNAME___ on ___DATE___.
//  Copyright (c) ___YEAR___ ___ORGANIZATIONNAME___. All rights reserved.
//

enum ___VARIABLE_sceneName___Action {

}

protocol ___VARIABLE_sceneName___ViewModelProtocol {

    // MARK: - Properties
    var coordinator: ___VARIABLE_sceneName___CoordinatorProtocol { get }
    
    // MARK: - Methods
    func handle(action: ___VARIABLE_sceneName___Action)

}

final class ___VARIABLE_sceneName___ViewModel: ___VARIABLE_sceneName___ViewModelProtocol {
    
    // MARK: - Properties
    internal var coordinator: ___VARIABLE_sceneName___CoordinatorProtocol

    // MARK: - Lifecycle
    init(coordinator: ___VARIABLE_sceneName___CoordinatorProtocol) {
        self.coordinator = coordinator
    }

    // MARK: - Methods
    func handle(action: ___VARIABLE_sceneName___Action) {

    }
}
